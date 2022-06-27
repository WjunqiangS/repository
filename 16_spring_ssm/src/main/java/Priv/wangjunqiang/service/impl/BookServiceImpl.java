package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.service.BookService;
import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.domain.Book;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookServiceImpl implements BookService {
    @Autowired
    private BookDao bookDao;

    @Override
    public Book findById(Integer id) {
        return bookDao.findById(id);
    }

    @Override
    public boolean insert(Book book) {
        return bookDao.insert(book);
    }

    @Override
    public boolean update(Book book) {
        return bookDao.update(book);
    }

    @Override
    public boolean delete(Integer id) {
        return bookDao.delete(id);
    }

    @Override
    public List<Book> findAll() {
        return bookDao.findAll();
    }
}
