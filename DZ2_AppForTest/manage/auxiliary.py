import hashlib
import os
import PyPDF2


class Auxiliary:
    @staticmethod
    def is_dict(o):
        """ If an object looks like dict, behaves like dict then return True else False """
        return True if hasattr(o, '__getitem__') and hasattr(o, '__setitem__') and hasattr(o, 'keys') else False

    @staticmethod
    def is_list(o):
        """ If an object looks like list, behaves like list then return True else False """
        return True if hasattr(o, '__getitem__') and hasattr(o, '__setitem__') and not hasattr(o, 'keys') else False

    @staticmethod
    def get_md5_sum(o):
        """ Get md5 sum of given file """
        if not os.path.isfile(o):
            return 'Given object is not a file'

        md5 = hashlib.md5()

        with open(o, 'rb') as fo:
            file_data = fo.read()

        md5.update(file_data)
        return md5.hexdigest()

    @staticmethod
    def get_self_location():
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @staticmethod
    def pdftotext(path_pdf, path_txt):

        if not os.path.isfile(path_pdf):
            raise FileNotFoundError

        with open(path_pdf, 'rb') as pdf:
            reader = PyPDF2.PdfFileReader(pdf)
            page_range = reader.getNumPages()
            with open(path_txt, 'a') as txt:
               for page in range(page_range - 1):
                   txt.write(reader.getPage(page).extractText())


if __name__ == '__main__':
    a = Auxiliary()
    samples_path = "C:\\Users\\fkutsepx\\Downloads\\Auriga_OlegLeontyev-pythonautomationcourse2017-a70550441d85\\Auriga_OlegLeontyev-pythonautomationcourse2017-a70550441d85\\src\\DZ2_AppForTest\\sample_data"

    pdf_sample = os.path.join(samples_path, 'test_2_sample.pdf')
    txt_sample = os.path.join(samples_path, 'test_2_sample.txt')
    pdf_result = os.path.join(samples_path, 'test_result.pdf')
    txt_result = os.path.join(samples_path, 'test_result.txt')

    a.pdftotext(pdf_sample, txt_sample)
    a.pdftotext(pdf_result, txt_result)

    print(a.get_md5_sum(txt_sample))
    print(a.get_md5_sum(txt_result))



