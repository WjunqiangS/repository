package Priv.wangjunqiang.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;
import org.springframework.stereotype.Controller;

@Configuration
// 防止SpringMVC和Spring配置重复加载Controller中的类
@ComponentScan({"Priv.wangjunqiang.service", "Priv.wangjunqiang.dao"})
@ComponentScan(value = "Priv.wangjunqiang",
    excludeFilters = @ComponentScan.Filter(
        type = FilterType.ANNOTATION,
        classes = {Controller.class})
)

// @ComponentScan("Priv.wangjunqiang")
public class SpringConfig {
}
