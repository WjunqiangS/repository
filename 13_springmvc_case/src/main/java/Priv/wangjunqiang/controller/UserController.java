package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;

@Controller
// 设置整体类的访问路径
@RequestMapping("/user")
public class UserController {

    // 设置具体类的访问路径
    @RequestMapping("/save")
    @ResponseBody
    public String save() {
        System.out.println("user save...");
        return "{'module':'user save'}";
    }

    @RequestMapping("/delete")
    @ResponseBody
    public String delete() {
        System.out.println("user delete...");
        return "{'module':'user delete'}";
    }

    @RequestMapping("/update")
    @ResponseBody
    public String update(String name, int age)
        throws UnsupportedEncodingException {
        // 处理get请求有中文的情况
        name =
            new String(name.getBytes("ISO8859-1"), StandardCharsets.UTF_8).trim();
        System.out.println("name ==>" + name);
        System.out.println("age ==>" + age);

        return "{'module':'user update'}";
    }

    @RequestMapping("/find")
    @ResponseBody
    // 当参数名不一样时 需要指定RequestParam
    public String find(@RequestParam("name") String name, int age) {
        System.out.println("name ==>" + name);
        System.out.println("age ==>" + age);

        return "{'module':'user find'}";
    }

    @RequestMapping("/get")
    @ResponseBody
    public String get(User user) {
        System.out.println("name ==>" + user.getName());
        System.out.println("age ==>" + user.getAge());

        return "{'module':'user find'}";
    }

    @RequestMapping("/getJsonPojo")
    @ResponseBody
    // 获取json对象 被装载到请求体里面
    // 同理可以设置List、数组等对象数据
    public String getJsonPojo(@RequestBody User user) {

        System.out.println(user);

        return "{'module':'user getJsonPojo'}";
    }
}
