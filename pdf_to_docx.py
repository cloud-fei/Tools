# python3 pdf_to_docx xxx.pdf

import argparse
from pdf2docx import Converter

def pdf_to_docx(input_pdf, output_docx):
    # 使用 Converter 将 PDF 转换为 Word 文档
    cv = Converter(input_pdf)
    cv.convert(output_docx, start=0, end=None)
    cv.close()
    print(f"Successfully converted {input_pdf} to {output_docx}")

def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description="Convert a PDF file to a Word document.")

    # 添加参数
    parser.add_argument("input_pdf", help="The input PDF file to be converted.")

    # 解析命令行参数
    args = parser.parse_args()

    # 构建输出文件名
    output_docx = args.input_pdf.replace(".pdf", ".docx")

    # 将 PDF 文件转换为 Word 文档
    pdf_to_docx(args.input_pdf, output_docx)

if __name__ == "__main__":
    main()
