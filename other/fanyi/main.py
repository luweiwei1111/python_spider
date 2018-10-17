#coding=utf-8
from google_translate import GoogleTranslate
from sqlite3_sql import Sql

if __name__ == "__main__":      
    google_translate = GoogleTranslate()

    content = """
    The version of IBM WebSphere Portal installed on the remote host is
7.0.0.x prior to 7.0.0.2 CF29. It is, therefore, affected by multiple
vulnerabilities :

  - A remote code execution vulnerability exists in the
    Apache Struts ClassLoader. A remote attacker can exploit
    this issue by manipulating the 'class' parameter of an
    ActionForm object to execute arbitrary code.
    (CVE-2014-0114)

  - A cross-site scripting vulnerability exists which allows
    a remote, authenticated attacker to inject arbitrary
    web script or HTML. (CVE-2014-0910)

  - An unspecified denial of service vulnerability exists
    that allows a remote attacker to crash the host by
    sending a specially crafted web request to cause a
    consumption of resources. (CVE-2014-0949)

  - A cross-site scripting vulnerability exists in the
    'boot_config.jsp' script due to improper validation of
    user-supplied input. An attacker can exploit this issue
    to execute arbitrary script code in the security context
    of a user's browser to steal authentication cookies.
    (CVE-2014-0952)

  - An unspecified cross-site scripting vulnerability exists
    due to improper validation of user-supplied input.
    (CVE-2014-0953)

  - A privilege escalation vulnerability exists in the Web
    Content Viewer portlet due to improper handling of JSP
    includes. A remote attacker can exploit this issue to
    obtain sensitive information, cause a denial of service,
    or control the request dispatcher by sending a specially
    crafted URL request. (CVE-2014-0954)

  - An unspecified cross-site scripting vulnerability exists
    due to improper validation of user-supplied input. An
    attacker can exploit this issue to execute arbitrary
    script code in the security context of a user's web
    browser to steal authentication cookies. (CVE-2014-0956)

  - An unspecified denial of service vulnerability exists
    that allows an authenticated attacker to cause a
    successful login to loop back to the login page
    indefinitely. (CVE-2014-0959)

  - An unspecified information disclosure vulnerability
    exists which allows a remote attacker to gain access to
    sensitive information. (CVE-2014-3083)

  - An unspecified cross-site scripting vulnerability
    exists due to improper validation of user-supplied
    input. An attacker can exploit this issue to execute
    arbitrary script code in the security context of a
    user's browser. (CVE-2014-3102)

  - An information disclosure vulnerability exists due to
    the returned error codes which an attacker can use to
    identify devices behind a firewall. (CVE-2014-4746)

  - An unspecified open redirect vulnerability exists that
    allows an attacker to perform a phishing attack by
    enticing a user to click on a malicious URL.
    (CVE-2014-4760)

  - An information disclosure vulnerability exists which
    allows a remote, authenticated attacker to gain access
    to sensitive information, such as user credentials,
    through certain HTML pages. (CVE-2014-4761)

  - An unrestricted file upload vulnerability exists which
    allows a remote, authenticated attacker to upload large
    files, potentially resulting in a denial of service.
    (CVE-2014-4792)

  - An unspecified vulnerability exists that allows an
    authenticated attacker to execute arbitrary code on the
    system. (CVE-2014-4808)

  - A flaw exists due to improper recursion detection during
    entity expansion. A remote attacker, via a specially
    crafted XML document, can cause the system to crash,
    resulting in a denial of service. (CVE-2014-4814)

  - An information disclosure vulnerability exists that
    allows a remote attacker to identify whether or not a
    file exists based on the web server error codes.
    (CVE-2014-4821)

  - An unspecified cross-site scripting vulnerability exists
    that allows a remote, authenticated attacker to execute
    arbitrary code via a specially crafted URL.
    (CVE-2014-6093)

  - An unspecified reflected cross-site scripting
    vulnerability exists due to improper validation of
    user-supplied input. A remote attacker can exploit this
    flaw using a specially crafted URL to execute arbitrary
    script code in a user's web browser within the security
    context of the hosting website. This allows an attacker
    to steal a user's cookie-based authentication
    credentials. (CVE-2014-6215)

  - An unspecified reflected cross-site scripting
    vulnerability exists due to improper validation of
    user-supplied input. A remote attacker can exploit this
    flaw using a specially crafted URL to execute arbitrary
    script code in a user's web browser within the security
    context of the hosting website. This allows an attacker
    to steal a user's cookie-based authentication
    credentials. (CVE-2014-8909)

  - An unspecified flaw exists that is trigged when handling
    Portal requests. A remote attacker can exploit this to
    cause a consumption of CPU resources, resulting in a
    denial of service condition. (CVE-2015-1943)
    """

    desc = google_translate.translate_cn(content, 'en')
    print(desc)
"""
    #update family
    family_cn = ''
    family_info = Sql.select_family()
    for familys in family_info:
        family = familys[0]
        print(family)
        family_cn = google_translate.translate_cn(family, 'en')
        print(family_cn)
        Sql.update_family_cn(family_cn, family)

    #对于不符合规范的翻译进行人工校准
    Sql.update_family_auth()
    """