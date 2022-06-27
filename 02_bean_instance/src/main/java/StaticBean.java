import Priv.wangjunqiang.dao.OrderDao;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * 静态工厂创建Bean对象
 */
public class StaticBean {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext("ApplicationContext.xml");

        OrderDao orderDao = (OrderDao)applicationContext.getBean("orderDao");

        orderDao.save();

    }
}
