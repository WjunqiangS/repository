package Priv.wangjunqiang.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
// 指定扫描Bean注解所在的目录
@ComponentScan({"Priv.wangjunqiang.dao", "Priv.wangjunqiang.aop"})
@EnableAspectJAutoProxy
public class SpringConfig {
}
