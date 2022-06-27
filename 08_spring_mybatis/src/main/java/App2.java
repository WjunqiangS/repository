import Priv.wangjunqiang.config.SpringConfig;
import Priv.wangjunqiang.domain.User;
import Priv.wangjunqiang.service.UserService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.util.List;

public class App2 {
    public static void main(String[] args) {
        // 1. 获取Spring注解类型的ApplicationContext并指定配置
        ApplicationContext applicationContext =
            new AnnotationConfigApplicationContext(SpringConfig.class);

        // 2.获取被Spring容器管理的Bean
        UserService userService = applicationContext.getBean(UserService.class);

        // 3.执行Bean中的方法
        List<User> user = userService.findByStatus("Y");
        // User user = userService.findById(1);

        System.out.println(user);
    }
}
