package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.service.BookService;

public class BookServiceImpl implements BookService {
    private BookDao bookDao;

    public BookServiceImpl() {
        System.out.println("book service construct...");
    }

    @Override
    public void save() {
        System.out.println("book service save...");
        bookDao.save();
    }

    public void setBookDao(BookDao bookDao) {
        this.bookDao = bookDao;
    }
}
