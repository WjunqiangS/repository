import Priv.wangjunqiang.dao.UserDao;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class InstanceBean {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext("ApplicationContext.xml");
        UserDao userDao = (UserDao)applicationContext.getBean("userDao");
        userDao.save();
    }
}
