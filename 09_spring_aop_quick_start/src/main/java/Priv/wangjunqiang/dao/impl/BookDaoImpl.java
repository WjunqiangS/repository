package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.BookDao;
import org.springframework.stereotype.Repository;

// 加载Bean到container容器中
@Repository
public class BookDaoImpl implements BookDao {
    @Override
    public void save() {
        System.out.println("book dao save....");
    }

    @Override
    public void update() {
        Integer ret = 1 / 0;
        System.out.println("book dao update...");
    }
}
