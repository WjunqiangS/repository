import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.service.BookService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext(
                "ApplicationContext.xml");

        BookDao bookService =
            (BookDao)applicationContext.getBean("bookDao");
        bookService.save();
    }
}
