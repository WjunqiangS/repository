package Priv.wangjunqiang;

import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.controller.UserController;
import Priv.wangjunqiang.service.UserService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext applicationContext =
            new AnnotationConfigApplicationContext(SpringConfig.class);

        System.out.println(applicationContext.getBean(UserService.class));
    }
}
