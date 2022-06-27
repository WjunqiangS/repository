package Priv.wangjunqiang.dao;

import Priv.wangjunqiang.domain.Book;

import java.util.List;

public interface BookDao {
    public Book findById(Integer id);
    public boolean insert(Book book);
    public boolean update(Book book);
    public boolean delete(Integer id);
    public List<Book> findAll();
}
