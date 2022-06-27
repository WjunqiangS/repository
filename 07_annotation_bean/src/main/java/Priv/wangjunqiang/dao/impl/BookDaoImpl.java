package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.BookDao;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

// 加载Bean到container容器中
@Repository("bookDao")
@Scope("singleton")
public class BookDaoImpl implements BookDao {
    @Value("${name}")
    private String database;
    @Override
    public void save() {
        System.out.println("book dao save...." + database);
    }
}
