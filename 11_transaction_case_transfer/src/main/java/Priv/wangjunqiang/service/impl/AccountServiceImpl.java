package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.dao.AccountDao;
import Priv.wangjunqiang.service.AccountService;
import Priv.wangjunqiang.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl implements AccountService {
    @Autowired
    private AccountDao accountDao;

    @Autowired
    private LogService logService;

    @Override
    public boolean inMoney(String name, double money) {
        return accountDao.inMoney(name, money);
    }

    @Override
    public boolean outMoney(String name, double money) {
        return accountDao.outMoney(name, money);
    }

    @Override
    public boolean transferMoney(String from, String dest, double money) {
        boolean flag = false;

        try {
            flag = outMoney(from, money);

            int i = 1/0;

            flag = inMoney(dest, money);
        } finally {
            logService.log(from, dest, 1000.0);
        }

        return flag;
    }
}
