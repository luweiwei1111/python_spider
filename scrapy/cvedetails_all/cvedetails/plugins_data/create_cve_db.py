
import os
import re
import sqlite3
import sys
import codecs

class cve_db:
    def __init__(self, db_path, plugin_dir, table_name):
    
        if os.path.exists(db_path):
            os.remove(db_path)
            
        self.cx = sqlite3.connect(db_path)
        self.cu = self.cx.cursor()
        self.table_name = table_name

        sql = """
            CREATE TABLE IF NOT EXISTS "%s"(
                         "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                         plugin_id       TEXT NOT NULL,
                         cve             TEXT NOT NULL,
                         file            TEXT NOT NULL);
        """ % table_name
        self.cu.execute(sql)
        self.cu.execute('CREATE INDEX index_cve on "%s" (cve);' % table_name)
        self.count = 0

        self.file_walk(plugin_dir)
        
        return

    def file_walk(self, rootdir):
        list = os.listdir(rootdir)
        for i in range(0,len(list)):
            path = os.path.join(rootdir,list[i])
            if os.path.isfile(path):
                if re.match(".*\.nasl$", path) is not None:
                    self.nasl_parse(path);
            elif os.path.isdir(path):
                self.file_walk(path)
                
    def nasl_parse(self, path):

        if 0 == self.count % 1000:
            print(self.count)
            
        self.count += 1
        self.path = path

        pf = codecs.open(path, 'r+', encoding = "ISO-8859-1")

        #初始化cves及id数据
        self.cves = None
        self.plugin_id = None
        
        #初始状态, 没有接续结束
        state = 1
        while True:
            line = pf.readline()
            if not line:
                break;
            if state > 0:
                state = self.description_parse(line, pf, state)
            else:
                break;
                
        #解析结束, 写数据库
        if 0 == state:
            result = re.match(".*/", path)
            path = path[result.span()[1]:len(path)]
            if self.cves is not None:
                if self.plugin_id is None:
                    self.plugin_id = "unknow"
                self.db_inset(path, self.cves.split(','), self.plugin_id)
            
        pf.close()

    def description_parse(self, line, pf, state):
    
        #检测注释
        line = line.lstrip()
        if  len(line) == 0 or '#' == line[0]:
            return state
    
        #查找 if (description) 或者 if (description) {
        if state == 1:
            ctx = re.search(r'(^|;)\s*if\s*\(description\)\s*$',line)
            if ctx:
                state = 2;
                return state
                
            ctx = re.search(r'(^|;)\s*if\s*\(description\)\s*{',line)
            if ctx:
                state = 3;
                line = line[ctx.span()[1]:]
    
        #已经查找到 if (description), 现在查找 {
        if state == 2:
             ctx = re.search(r'\s*{',line);
             if ctx:
                state = 3;
                line = line[ctx.span()[1]:]
    
        #已经查找到  if (description) {, 现在匹配相关数据，并且查找 }
        if state == 3:
            while 1:
                if re.search(r'^\s*}', line):
                    state = 0
                    break
                    
                end_line = self.tag_parse(line, pf)
    
                if end_line:
                    line = end_line
                    if re.search(r'^\s*}', end_line):
                        state = 0
                        break
                else:
                    break;
    
        return state
    
    #检测格式tag(ddd){}
    def tag_parse(self, line, pf):

        #这部分不能缺少
        line, end_line = self.get_full_tag(line, pf)
        
        if self.cves != None and self.plugin_id != None:
            return end_line
            
        line = line.strip()
        
        #判断空白行或者注释
        if len(line) <= 0 or line[0] == "#":
            return end_line

        if self.tag_check(line, "script_id") or self.tag_check(line, "script_oid"):
            line = line.replace("script_id",""); 
            line = line.replace("script_oid","");
            line = line.replace('"',"");
            line = line.replace("'","");
            line = line.replace('(',"");
            line = line.replace(")","");
            line = line.replace('\r',"");
            line = line.replace("\n","");
            self.plugin_id = line

        elif self.tag_check(line, "script_cve_id"):
            line = line.replace("script_cve_id","");
            line = line.replace('"',"");
            line = line.replace("'","");
            line = line.replace('(',"");
            line = line.replace(")","");
            line = line.replace('\r',"");
            line = line.replace("\n","");
            self.cves = line

        return end_line

    def tag_check(self, line, pattern):
        match = r'^\s*'+ pattern + r'\s*\('
        ctx = re.search(match, line)
        if ctx:
            return True
        return False

    def get_full_tag(self, line, pf):
        stack = ''
        tmpline=""
        endline = None

        while True:
            stack, newline, endline = self.line_check(line, pf, stack)
            tmpline += newline

            if len(stack) == 0:
                break;
            line = pf.readline()
            if not line:
                print(self.path + "   ------>parse faild!!!!!")
                break;
            
        return tmpline, endline
        
    def line_check(self, line, pf, stack):
    
        set = '(){}\"\'#;'
        tmpline = ""
        endline = None

        for i in range(len(line)):
            char = line[i]
            if len(stack) > 0:
                if stack[-1] == '#':
                    if char == '\n':
                        stack = stack[0:-1]
                    continue;
                elif stack[-1] == '"':
                    if char == '"':
                        if line[i-1] != '\\':
                            stack = stack[0:-1]
                    tmpline += char
                    continue;
                elif stack[-1] == "'":
                    if char == "'":
                        if line[i-1] != '\\':
                            stack = stack[0:-1]
                    tmpline += char
                    continue
                    
            if char in set:
                if char == '#':
                    stack += char
                    continue
                    
                if char == ')':
                    if stack[-1] != '(':
                        print(os.path.basename(pf.name) + ':parse error ) !!\n')
                    stack = stack[0:-1]
                elif char == '}':
                    if stack[-1] != '{':
                        print(os.path.basename(pf.name) + ':parse error } !!\n')
                    stack = stack[0:-1]
                elif char ==';':
                    if len(stack) == 0:
                        endline = line[i+1: len(line)]
                        break;
                else:
                    stack += char
                    
            tmpline += char
        return stack, tmpline, endline

    def db_inset(self, path, cves, id):
        cve_str = ""
        for cve in cves:
            cve_str = cve_str + cve.strip() + ","

        cve_str = cve_str[0:-1]
        
        sql = "insert into %s (plugin_id, cve, file) values ('%s', '%s', '%s');" % (self.table_name, id, cve_str, path)
        self.cu.execute(sql)
        
    def db_close(self):
        self.cu.close()
        self.cx.commit()
        self.cx.close()
        return


if __name__ == '__main__':

    if len(sys.argv) < 4:
        print("commad format: python create_cve_db.py db_file, plugin_path, table_name\n")
        exit(0)
    db = cve_db(sys.argv[1], sys.argv[2], sys.argv[3])
    db.db_close()







