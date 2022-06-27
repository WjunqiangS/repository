package Priv.wangjunqiang.factory;

import Priv.wangjunqiang.dao.UserDao;
import Priv.wangjunqiang.dao.impl.UserDaoImpl;

public class UserDaoFactory {
    UserDaoFactory() {
        System.out.println("UserDao Factory...");
    }

    public UserDao getUserDao() {
        return new UserDaoImpl();
    }
}
