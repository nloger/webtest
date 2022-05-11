HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="css/default.css" rel="stylesheet" type="text/css" />
    <link href="css/main_report.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div class="bg">
<div class="d_nav">
<table cellpadding="0" cellspacing="1"> <tr><th>No</th><th>URL</th><th>Status</th></tr>
%(table)s
</table>
</div>
</div>
</body>
</html>"""


