package Priv.wangjunqiang.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
// 指定扫描Bean注解所在的目录
@ComponentScan({"Priv.wangjunqiang.service", "Priv.wangjunqiang.dao"})
@PropertySource("classpath:jdbc.properties")
public class SpringConfig {
}
