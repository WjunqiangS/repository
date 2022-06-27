package Priv.wangjunqiang.domain;

import java.sql.Date;

public class User {
    /**
     * 用户id
     */
    private Integer uid;
    /**
     * 用户名
     */
    private String username;
    /**
     * 密码
     */
    private String password;
    /**
     * 姓名
     */
    private String name;
    /**
     * 生日
     */
    private Date birthday;
    /**
     * 性别
     */
    private String sex;
    /**
     * 电话号码
     */
    private String telephone;
    /**
     * 邮箱
     */
    private String email;
    /**
     * 激活状态 Y表示激活，N表示未激活
     */
    private String status;
    /**
     * 激活码（唯一）
     */
    private String code;

    /**
     * 无参构造函数
     */
    public User() {
    }

    /**
     * @param uid 用户id
     * @param username 用户名
     * @param password 密码
     * @param name 姓名
     * @param birthday 生日
     * @param sex 性别
     * @param telephone 电弧
     * @param email 邮箱
     * @param status 激活状态
     * @param code 激活码
     */
    public User(Integer uid, String username, String password, String name,
        Date birthday, String sex, String telephone, String email,
        String status, String code) {
        this.uid = uid;
        this.username = username;
        this.password = password;
        this.name = name;
        this.birthday = birthday;
        this.sex = sex;
        this.telephone = telephone;
        this.email = email;
        this.status = status;
        this.code = code;
    }

    public Integer getUid() {
        return uid;
    }

    public void setUid(Integer uid) {
        this.uid = uid;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    @Override
    public String toString() {
        return "Priv.wangjunqiang.domain.User{" + "uid=" + uid + ", username='" + username + '\''
            + ", password='" + password + '\'' + ", name='" + name + '\''
            + ", birthday=" + birthday + ", sex='" + sex + '\''
            + ", telephone='" + telephone + '\'' + ", email='" + email + '\''
            + ", status='" + status + '\'' + ", code='" + code + '\'' + '}';
    }
}
