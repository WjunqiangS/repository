package Priv.wangjunqiang.dao.impl;

import Priv.wangjunqiang.dao.UserDao;
import Priv.wangjunqiang.domain.User;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class UserDaoImpl implements UserDao {
    @Override
    public User findById(int id) {
        return null;
    }

    @Override
    public List<User> findByStatus(String status) {
        return null;
    }
}
