package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.Book;
import Priv.wangjunqiang.exception.BusinessException;
import Priv.wangjunqiang.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {

    @Autowired
    private BookService bookService;

    @GetMapping("/{id}")
    public Result findById(@PathVariable Integer id) {

        if (id < 0) {
            // 抛出异常给ExceptionAdvice类处理
            throw new BusinessException(ResultCode.BUSINESS_EXCEPTION,
                "请你好好传入参数，别惹我");
        }

        Book book = bookService.findById(id);

        // 异常处理案例
        // try {
        //     int i = 1 / 0;
        // } catch (Exception e) {
        //     throw new SystemException(ResultCode.SYSTEM_EXCEPTION,
        //         "系统维护，请稍后再试");
        // }

        Integer code = book != null? ResultCode.GET_OK : ResultCode.GET_ERR;

        return new Result(code, book);
    }
    @PostMapping
    public Result insert(@RequestBody Book book) {
        boolean flag = bookService.insert(book);

        return new Result(flag? ResultCode.SAVE_OK: ResultCode.SAVE_ERR, flag);
    }
    @PutMapping
    public Result update(@RequestBody Book book) {
        boolean flag = bookService.update(book);

        return new Result(flag? ResultCode.UPDATE_OK: ResultCode.UPDATE_ERR,
            flag);
    }
    @DeleteMapping("/{id}")
    public Result delete(@PathVariable Integer id) {
        boolean flag = bookService.delete(id);

        return new Result(flag? ResultCode.DELETE_OK: ResultCode.DELETE_ERR,
            flag);
    }
    @GetMapping
    public Result findAll() {
        List<Book> bookList = bookService.findAll();

        Integer code = bookList != null? ResultCode.GET_OK : ResultCode.GET_ERR;

        return new Result(code, bookList);
    }
}
