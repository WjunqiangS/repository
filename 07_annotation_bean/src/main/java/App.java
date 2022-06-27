import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.service.BookService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext applicationContext =
            new AnnotationConfigApplicationContext(SpringConfig.class);

        applicationContext.registerShutdownHook();

        BookService bookService =
            applicationContext.getBean(BookService.class);
        bookService.save();
    }
}
