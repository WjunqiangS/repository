import Priv.wangjunqiang.service.BookService;
import Priv.wangjunqiang.service.impl.BookServiceImpl;

public class App {
    public static void main(String[] args) {
        BookService bookService = new BookServiceImpl();
        bookService.save();
    }
}
