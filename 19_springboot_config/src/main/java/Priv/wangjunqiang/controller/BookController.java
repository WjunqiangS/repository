package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.Enterprise;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/books")
public class BookController {

    // 使用层级的形式获取配置文件的数据
    @Value("${server.port}")
    private Integer port;

    @Autowired
    private Enterprise enterprise;

    @GetMapping("/{id}")
    public String findById(@PathVariable Integer id) {
        System.out.println(port);
        System.out.println(enterprise);
        System.out.println("id ===> " + id);
        return "Hello SpringBoot Start";
    }
}
