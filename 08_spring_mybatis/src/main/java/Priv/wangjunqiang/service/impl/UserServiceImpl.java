package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.dao.UserDao;
import Priv.wangjunqiang.domain.User;
import Priv.wangjunqiang.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserDao userDao;

    @Override
    public User findById(int id) {
        return userDao.findById(id);
    }

    @Override
    public List<User> findByStatus(String status) {
        return userDao.findByStatus(status);
    }
}
