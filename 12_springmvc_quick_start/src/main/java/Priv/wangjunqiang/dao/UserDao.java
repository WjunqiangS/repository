package Priv.wangjunqiang.dao;

import Priv.wangjunqiang.domain.User;

import java.util.List;

public interface UserDao {
    // @Select("select * from tab_user where uid = #{id}")
    public User findById(int id);

    // @Select("select * from tab_user where status = #{status}")
    public List<User> findByStatus(String status);
}
