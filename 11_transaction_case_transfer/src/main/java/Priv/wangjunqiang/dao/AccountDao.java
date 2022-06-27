package Priv.wangjunqiang.dao;

import org.apache.ibatis.annotations.Param;

public interface AccountDao {
    public boolean inMoney(@Param("name") String name,
        @Param("money") Double money);

    public boolean outMoney(@Param("name") String name,
        @Param("money") Double money);
}
