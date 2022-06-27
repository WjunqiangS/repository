package Priv.wangjunqiang.service;

import Priv.wangjunqiang.domain.User;

import java.util.List;

public interface UserService {
    public User findById(int id);
    public List<User> findByStatus(String status);
}
