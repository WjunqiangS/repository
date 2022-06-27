package priv.wangjunqiang.service;

import Priv.wangjunqiang.domain.Book;
import Priv.wangjunqiang.service.BookService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class BookServiceTest {
    @Autowired
    private BookService bookService;

    @Test
    public void findById() {
        System.out.println(bookService.findById(1));
    }

    @Test
    public void insert() {
        Book book = new Book();
        book.setDescription("Test");
        book.setName("测试书籍");
        book.setType("测试类型");
        System.out.println(bookService.insert(book));
    }

    @Test
    public void update() {
        Book book = new Book();
        book.setId(13);
        book.setDescription("Test Update");
        book.setName("测试书籍2");
        book.setType("测试类型update");
        System.out.println(bookService.update(book));
    }

    @Test
    public void delete() {
        System.out.println(bookService.delete(13));
    }

    @Test
    public void findAll() {
        System.out.println(bookService.findAll());
    }
}
