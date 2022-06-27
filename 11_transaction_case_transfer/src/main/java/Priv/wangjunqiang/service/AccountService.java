package Priv.wangjunqiang.service;

import org.springframework.transaction.annotation.Transactional;

public interface AccountService {
    boolean inMoney(String name, double money);
    boolean outMoney(String name, double money);
    // 开启事务
    @Transactional()
    boolean transferMoney(String from, String dest, double money);
}
