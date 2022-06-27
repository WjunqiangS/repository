package Priv.wangjunqiang.service.impl;

import Priv.wangjunqiang.dao.LogDao;
import Priv.wangjunqiang.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LogServiceImpl implements LogService {
    @Autowired
    private LogDao logDao;

    @Override
    public boolean log(String from, String dest, Double money) {
        return logDao.log(from + "账号转账" + money + "元到" + dest + "账号");
    }
}
