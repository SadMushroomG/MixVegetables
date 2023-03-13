using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MushroomLab
{
    class C03_DataType
    {
        /*
         * C#中的数据类型:
         * 值类型      ValueTypes
         * 引用类型    ReferenceTypes
         * 指针类型    PointerTypes
         */

        /*
         * 值类型
         * 可以直接分配一个值
         * 派生于System.ValueType
         * 包含数据，如int、char、float分别储存数字、字符、浮点数
         * 声明int时系统分配内存来储存值
         */

        /*
         * 类型       / 描述                                / 范围    / 默认值
         * bool         布尔值
         * byte         8位无符号整数
         * char         16位Unicode字符
         * decimal      128位精确的十进制，28-29有效位数
         * double       64位双精度浮点型
         * float        32位单精度浮点型
         * int          32位有符号整数类型
         * long         64位有符号整数类型
         * sbyte        8位有符号整数类型
         * short        16位有符号整数类型
         * uint         32位无符号整数类型
         * ulong        64位无符号整数类型
         * ushort       16位无符号整数类型
         */

        public void printSizeOfTypes()
        {
            Console.WriteLine(sizeof(int));
            Console.WriteLine(sizeof(decimal));
            Console.WriteLine(sizeof(ulong));
        }

        /*
         * 引用类型
         * 不包含储存在变量中的实际数据，但包含对变量的引用
         * 指的是一个内存位置
         * 内置的引用类型：object, dynamic, string
         */

        public void ReferenceDataType()
        {
            //object是C#通用类型系统（Common Type System - CTS）的终极基类
            //System.Object => object
            //object可以被分配任何其他类型的值
            //分配前需要先进行类型转换
            //值类型转换为对象类型时被称为装箱
            //对象类型被转换为值类型时被称为拆箱
            object obj;
            obj = 100; //装箱

            //dynamic的类型检查在运行时发生
            //object的类型检查在编译时发生
            dynamic d = 20;
        
        }

        //public void StringType()
        //{
        //    String str = "MushroomLab";
        //    str = str;
        //}

    }
}
