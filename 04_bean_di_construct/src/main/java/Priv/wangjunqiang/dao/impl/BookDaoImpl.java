package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.BookDao;

public class BookDaoImpl implements BookDao {
    private String databaseName;
    private int port;

    public BookDaoImpl(String databaseName, int port) {
        this.databaseName = databaseName;
        this.port = port;
    }

    @Override
    public void save() {
        System.out.println("book dao save....");
    }
}
