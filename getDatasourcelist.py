cells = AdminConfig.list('Cell').split()
datasources = []
for cell in cells:
    cn = AdminConfig.showAttribute(cell, 'name')
    print cn
    datasources.append(AdminConfig.list('DataSource',cell).splitlines())