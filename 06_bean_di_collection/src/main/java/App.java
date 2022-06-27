import Priv.wangjunqiang.dao.BookDao;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext(
                "ApplicationContext.xml");

        BookDao bookDao =
            (BookDao)applicationContext.getBean("bookDao");
        bookDao.save();
    }
}
