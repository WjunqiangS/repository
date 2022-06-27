package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
// 设置整体类的访问路径
@RequestMapping("/book")
public class BookController {

    // 设置具体类的访问路径
    @RequestMapping("/save")
    @ResponseBody
    public String save() {
        System.out.println("Book save...");
        return "{'module':'book save'}";
    }

    @RequestMapping("/delete")
    @ResponseBody
    public String delete() {
        System.out.println("Book delete...");
        return "{'module':'book delete'}";
    }


}
