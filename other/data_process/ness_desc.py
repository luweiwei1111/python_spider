import sys
import os
import os.path

class Ness:
    def read_ness(self, file):
        data_desc = ''
        with open(file, 'r') as f1:
            list_text = f1.readlines()
            
        desc_flag = False
        desc_head = 'include("ns_compat.inc");\n\n'
        for line in list_text:
            if 'description' in line and 'if' in line and '(' in line and ')' in line and 'NASL_LEVEL' not in line and '1' not in line and '0' not in line and ';' not in line:
                desc_flag = True
            if desc_flag == True:
                data_desc = data_desc + line
                if 'exit(0)' in line or  'exit (0);' in line:
                    data_desc = desc_head + data_desc + '\n}'
                    break

        data_desc = data_desc.replace('|', '')
        #print(data_desc)

        if desc_flag == True:
            #写数据
            with open(file, 'w') as f:
                f.write(data_desc)

if __name__ == '__main__':
    NESS_PATH = '/usr/local/var/lib/openvas/plugins/'
    ness = Ness()

    count = 0
    for filename in os.listdir(NESS_PATH):
           if os.path.splitext(filename)[1] == '.nasl':
               count = count + 1
               script_file = NESS_PATH + filename
               print('process->' + str(count))
               ness.read_ness(script_file)