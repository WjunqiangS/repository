import Priv.wangjunqiang.service.BookService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class ConstrctBean {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new ClassPathXmlApplicationContext("ApplicationContext.xml");

        BookService bookService =
            (BookService)applicationContext.getBean("bookService");
        bookService.save();

    }
}
