package Priv.wangjunqiang.factory;

import Priv.wangjunqiang.dao.UserDao;
import Priv.wangjunqiang.dao.impl.UserDaoImpl;
import org.springframework.beans.factory.FactoryBean;

public class UserDaoFactoryBean implements FactoryBean<UserDao> {

    UserDaoFactoryBean() {
        System.out.println("user Dao Factory Bean...");
    }

    @Override
    public UserDao getObject() throws Exception {
        return new UserDaoImpl();
    }

    @Override
    public Class<?> getObjectType() {
        return UserDao.class;
    }

    @Override
    public boolean isSingleton() {
        return true;
    }
}
