import Priv.wangjunqiang.service.BookService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App2 {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext("ApplicationContext.xml.back");
        // BookDao bookDao = (BookDao)applicationContext.getBean("bookDao");
        // bookDao.save();

        BookService bookService =
            applicationContext.getBean(BookService.class);
        bookService.save();
        // System.out.println(bookService);

    }
}
