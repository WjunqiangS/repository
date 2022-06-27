import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.service.BookService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App2 {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext("ApplicationContext.xml");
        // BookDao bookDao = (BookDao)applicationContext.getBean("bookDao");
        // bookDao.save();

        BookService bookService =
            (BookService)applicationContext.getBean("bookService");
        bookService.save();

    }
}
