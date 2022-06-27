package Priv.wangjunqiang.service;

import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

public interface LogService {
    // 重新申请一个事务，确保Service层的回滚不会一起回滚
    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public boolean log(String from, String dest, Double money);
}
