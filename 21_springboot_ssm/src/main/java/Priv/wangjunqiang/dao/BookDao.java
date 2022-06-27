package Priv.wangjunqiang.dao;

import Priv.wangjunqiang.domain.Book;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BookDao {
    public Book findById(Integer id);
    public boolean insert(Book book);
    public boolean update(Book book);
    public boolean delete(Integer id);
    public List<Book> findAll();
}
