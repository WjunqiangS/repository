package Priv.wangjunqiang;

import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.service.AccountService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class AccountServiceTest {

    @Autowired
    private AccountService accountService;

    @Test
    public void inMoneyTest() {
        System.out.println(accountService.inMoney("Tom", 1000));
    }

    @Test
    public void outMoneyTest() {
        accountService.outMoney("Tom", 1000);
    }

    @Test
    public void transferMoneyTest() {
        System.out.println(accountService.transferMoney("Jerry", "Tom", 1000));
    }
}
