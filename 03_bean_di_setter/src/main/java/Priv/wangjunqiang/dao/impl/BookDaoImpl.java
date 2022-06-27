package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.BookDao;

public class BookDaoImpl implements BookDao {
    private String databaseName;
    private int port;

    @Override
    public void save() {
        System.out.println("book dao save....");
    }

    public String getDatabaseName() {
        return databaseName;
    }

    public void setDatabaseName(String databaseName) {
        this.databaseName = databaseName;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
}
