package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.Book;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@CrossOrigin(origins = "*", maxAge = 3600)
@RestController
@RequestMapping("/books")
public class BookController {

    @PostMapping
    public String save(@RequestBody Book book) {
        System.out.println(book);
        return "{'module' : 'book save successfully'}";
    }

    @GetMapping
    public List<Book> getAll() {
        List<Book> list = new ArrayList<>();

        Book book = new Book();
        book.setId(1);
        book.setName("C++ primary plus");
        book.setType("编程书籍");
        book.setDescription("C++实战开发");
        list.add(book);

        Book book1 = new Book();
        book1.setId(1);
        book1.setName("vim实用技巧");
        book1.setType("vim操作");
        book1.setDescription("vim是最快编辑器之一");
        list.add(book1);

        return list;
    }
}
