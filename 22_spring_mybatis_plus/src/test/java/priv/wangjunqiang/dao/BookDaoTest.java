package priv.wangjunqiang.dao;

import Priv.wangjunqiang.dao.BookDao;
import Priv.wangjunqiang.domain.Book;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@SpringBootTest
public class BookDaoTest {
    @Autowired
    private BookDao bookDao;

    @Test
    public void findById() {
        Book book = bookDao.selectById(1L);
        System.out.println(book);
    }

    @Test
    public void findAll() {
        // 写条件的函数
        // LambdaQueryWrapper<Book> bookLambdaQueryWrapper =
        //     new LambdaQueryWrapper<>();
        // 查询条件 ge gt eq lt le like likeLeft likeRight between
        // bookLambdaQueryWrapper.gt(Book::getId, 30);
        // bookLambdaQueryWrapper.lt(Book::getId, 3).or().ge(Book::getId, 33);
        // 查询投影
        // bookLambdaQueryWrapper.select(Book::getId, Book::getName);
        // bookLambdaQueryWrapper.like(Book::getName, "Mybatis");
        // List<Book> bookList = bookDao.selectList(bookLambdaQueryWrapper);
        // System.out.println(bookList);

        QueryWrapper<Book> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("count(*) as count", "type");
        queryWrapper.groupBy("type");
        // queryWrapper.gt("id", 30);
        List<Map<String, Object>> count = bookDao.selectMaps(queryWrapper);
        // long count = bookDao.selectCount(queryWrapper);
        System.out.println(count);
    }

    @Test
    public void update() {
        // Book book = new Book();
        // book.setId(30L);
        // book.setType("数据库操作");
        // book.setName("Mybatis Plus实战");
        // book.setDescription("Mybatis Plus 增删改查");

        Book book = bookDao.selectById(32);
        Book book2 = bookDao.selectById(32);

        book.setName("book 111");
        bookDao.updateById(book);

        book2.setName("book 222");
        bookDao.updateById(book2);

    }

    @Test
    public void delete() {
        bookDao.deleteById(32);
    }

    @Test
    public void save() {
        Book book = new Book();
        book.setType("数据库操作");
        book.setName("Mybatis Plus实战");
        book.setDescription("Mybatis Plus 增删改查");
        bookDao.insert(book);
    }

    @Test
    public void findByPage() {
        IPage<Book> iPage = new Page<>(1, 5);
        bookDao.selectPage(iPage, null);

        System.out.println("总共多少页:" + iPage.getPages());
        System.out.println("每页显示条数:"+ iPage.getSize());
        System.out.println("当前页:" + iPage.getCurrent());
        System.out.println("总条数:" + iPage.getTotal());
        System.out.println("数据:" + iPage.getRecords());
    }

}
