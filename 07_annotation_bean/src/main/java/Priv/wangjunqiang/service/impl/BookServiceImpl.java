package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

// 加载Bean到container中
@Service
public class BookServiceImpl implements BookService {

    @Autowired
    // 加载指定名称的Bean
    @Qualifier("bookDao")
    private BookDao bookDao;

    @Value("wangjunqiang")
    private String name;

    @Override
    public void save() {
        System.out.println("book service save..." + name);
        bookDao.save();
    }

    @PostConstruct
    public void init() {
        System.out.println("init...");
    }

    @PreDestroy
    public void destroy() {
        System.out.println("destroy...");
    }

    public void setBookDao(BookDao bookDao) {
        this.bookDao = bookDao;
    }
}
