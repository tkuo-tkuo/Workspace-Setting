set relativenumber
set list

set expandtab
set tabstop=4
set ai

syntax on

nnoremap <S-Tab> <<
nnoremap <S-Up> :m-2<CR>
nnoremap <S-Down> :m+<CR>

inoremap <S-Tab> <C-d>
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O
