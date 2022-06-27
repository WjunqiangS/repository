package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.domain.User;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    @GetMapping("/{id}")
    public User findUserById(@PathVariable Integer id) {
        User user = new User(id, "王俊强", 27);

        return user;
    }

    @GetMapping
    public List<User> findUsers() {
        List<User> list = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            list.add(new User( "王俊强", 27));
        }

        return list;
    }

    @PostMapping
    public String addUser(@RequestBody User user) {

        System.out.println(user);

        return "{'msg':'add successfully', 'status': '200'}";
    }

    @PutMapping
    public String modifyUser(@RequestBody User user) {
        System.out.println(user);
        return "{'msg': 'modify successfully', 'status': '200'}";
    }

    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable Integer id) {
        return "{'msg': 'delete successfully', 'status': '200'}";
    }
}
