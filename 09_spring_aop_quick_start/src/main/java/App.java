import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.dao.BookDao;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new AnnotationConfigApplicationContext(SpringConfig.class);
        BookDao bookDao = applicationContext.getBean(BookDao.class);
        bookDao.update();
        // bookDao.save();
    }
}
