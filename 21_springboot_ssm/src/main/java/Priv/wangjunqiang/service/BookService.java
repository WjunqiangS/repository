package Priv.wangjunqiang.service;

import Priv.wangjunqiang.domain.Book;

import java.util.List;

public interface BookService {
    public Book findById(Integer id);
    public boolean insert(Book book);
    public boolean update(Book book);
    public boolean delete(Integer id);
    public List<Book> findAll();
}
