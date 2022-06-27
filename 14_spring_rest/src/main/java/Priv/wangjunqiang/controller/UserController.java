package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

// 简化开发

// @Controller
// @ResponseBody
@RestController
@RequestMapping("/users")
public class UserController {

    // @RequestMapping(value = "/users/{id}", method = RequestMethod.GET)
    // @ResponseBody
    @GetMapping("/{id}")
    public User findUserById(@PathVariable Integer id) {
        User user = new User(id, "王俊强", 27);

        return user;
    }

    // @RequestMapping(value = "/users", method = RequestMethod.GET)
    // @ResponseBody
    @GetMapping
    public List<User> findUsers() {
        List<User> list = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            list.add(new User( "王俊强", 27));
        }

        return list;
    }


    // @RequestMapping(value = "/users", method = RequestMethod.POST)
    // @ResponseBody
    // @RequestBody 获取request发送的json数据
    @PostMapping
    public String addUser(@RequestBody User user) {

        System.out.println(user);

        return "{'msg':'add successfully', 'status': '200'}";
    }

    // @RequestMapping(value = "/users", method = RequestMethod.PUT)
    // @ResponseBody
    @PutMapping
    public String modifyUser(@RequestBody User user) {
        System.out.println(user);
        return "{'msg': 'modify successfully', 'status': '200'}";
    }

    // @RequestMapping(value = "/users/{id}", method = RequestMethod.DELETE)
    // @ResponseBody
    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable Integer id) {
        return "{'msg': 'delete successfully', 'status': '200'}";
    }
}
