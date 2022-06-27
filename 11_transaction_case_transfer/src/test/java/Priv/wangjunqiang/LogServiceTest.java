package Priv.wangjunqiang;

import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.dao.LogDao;
import Priv.wangjunqiang.service.LogService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = SpringConfig.class)
public class LogServiceTest {
    @Autowired
    private LogService logService;
    @Test
    public void logTest() {
        logService.log("Tim", "Jerry", 1000.0);
    }
}
