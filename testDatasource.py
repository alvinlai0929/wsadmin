#https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-testing-data-source-connections-using-wsadmin

ds = AdminConfig.getid('/DataSource:DS1/')
AdminControl.testConnection(ds)